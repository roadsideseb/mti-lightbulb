var api_version = "1";

(function () {
    var Benchmark,
        benchmarkQuery,
        queryParams;

    var parseQueryString = function(queryString) {
        var params = {}, queries, temp, i, l;
        // Split into key/value pairs
        queries = queryString.replace('?', '').split("&");
        // Convert the array of strings into an object
        for ( i = 0, l = queries.length; i < l; i++ ) {
            temp = queries[i].split('=');
            params[temp[0]] = temp[1];
        }
        return params;
    };

    var filterBenchmarks = function(app, vendor, version, object) {
        with (object.attributes) {
            if (database_vendor === vendor && app_label === app &&
                    django_version === version) {
                return true;
            }
            return false;
        }
    };

    Parse.initialize(parseComAppId, parseComJsKey);

    queryParams = parseQueryString(window.location.search);

    Benchmark = Parse.Object.extend("Benchmark");
    benchmarkQuery = new Parse.Query(Benchmark);
    benchmarkQuery.equalTo(
        "hostname",
        queryParams.hostname ? queryParams.hostname : 'mti'
    ).limit(500);


    var GraphView = Backbone.View.extend({

        initialize: function(options) {
            this.el = options.el;
            this.data = options.data || {};
        },

        render: function() {
            var dbVendor = this.$el.data('vendor'),
                appLabel = this.$el.data('app'),
                self = this;

            nv.addGraph(function() {
                var chart = nv.models.multiBarChart()
                    .showControls(false)
                    .showYAxis(true);

                chart.xAxis
                    .axisLabel('Number of models')
                    .tickFormat(d3.format(',f'));

                chart.yAxis
                    .axisLabel('SELECT query time (s)')
                    .tickFormat(d3.format(',.3f'));

                chart.yAxis.axisLabelDistance(25);

                d3.select($('svg', self.el)[0])
                    .datum(self.data[appLabel][dbVendor])
                    .call(chart);

                nv.utils.windowResize(chart.update);

                return chart;
            });
            return this;
        },
    });

    var getUniqueValues = function(collection, attribute) {
        var uniqueValues = _.uniq(collection,
                function(obj) { return obj.get(attribute); });
        return _.map(uniqueValues,
                function(obj) { return obj.get(attribute); });
    };

    benchmarkQuery.find({
        success: function (benchmarks) {
            var aggregatedData = {},
                betterSorted = {},
                dbs = getUniqueValues(benchmarks, 'database_vendor'),
                apps = getUniqueValues(benchmarks, 'app_label'),
                versions= getUniqueValues(benchmarks, 'django_version'),
                views = [],
                i, bm;

            _.each(apps, function(app) {
                betterSorted[app] = {};
                _.each(dbs, function(db) {
                    betterSorted[app][db] = [];
                    _.each(versions, function(version) {
                        var filterBms = _.filter(
                            benchmarks,
                            _.bind(filterBenchmarks, null, app, db, version)
                        );
                        if (filterBms.length > 0) {
                            betterSorted[app][db].push({
                                key: "Django " + filterBms[0].get('django_version'),
                                values: _.map(filterBms, function(model) {
                                    return {
                                        x: model.attributes.num_models,
                                        y: model.attributes.query_time_sql
                                    };
                                }).sort(function(a, b) { return a.x - b.x; })
                            });
                        }
                    });
                });
            });

            $('.mti-chart').each(function(idx) {
                new GraphView({el: $(this), data: betterSorted}).render();
            });
        }
    });
})();
