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


    benchmarkQuery.find({
        success: function (benchmarks) {
            var aggregatedData = {},
                idNameMap = {},
                sortedData = {},
                rawData = [],
                i, bm;

            for (i=0; i < benchmarks.length; i++) {
                with (benchmarks[i].attributes) {
                    idNameMap[test_id] = app_label + " Django " + django_version;
                };
            }

            var dbs = _.map(_.uniq(benchmarks, function(bm) { return bm.attributes.database_vendor }),
                    function(bm) { return bm.attributes.database_vendor });
            var apps = _.map(_.uniq(benchmarks, function(bm) { return bm.attributes.app_label}),
                    function(bm) { return bm.attributes.app_label });
            var versions = _.map(_.uniq(benchmarks, function(bm) { return bm.attributes.django_version}),
                    function(bm) { return bm.attributes.django_version});

            var betterSorted = {};

            _.each(apps, function(app) {
                betterSorted[app] = {}
                _.each(dbs, function(db) {
                    betterSorted[app][db] = []
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
                                    }
                                }).sort(function(a, b) { return a.x - b.x })
                            });
                        };
                    });
                });
            });

            console.log(rawData);

            var createChart = function(selector, data) {
                var dbVendor = $(selector).data('vendor'),
                    appLabel = $(selector).data('app');

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

                    d3.select($('svg', selector)[0])
                        .datum(data[appLabel][dbVendor])
                        .call(chart);

                    nv.utils.windowResize(chart.update);

                    return chart;
                });
            };

            $('.mti-chart').each(function() {
                createChart($(this), betterSorted);
            });
        }
    });
})();
