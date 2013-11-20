var api_version = "1";

(function () {
    Parse.initialize(parseComAppId, parseComJsKey);

    var Benchmark = Parse.Object.extend("Benchmark");
    var BenchmarkCollection = Parse.Collection.extend({
        model: Benchmark
    });
    var benchmarks = new BenchmarkCollection();
    benchmarks.fetch({
        success: function (benchmarks) {
            var aggregatedData = {};
            benchmarks.each(function (object) {
                var bm = object.attributes;
                console.log('Benchmark:', bm);

                var test_name = bm.app_label + " Django " + bm.django_version + " " + bm.database_vendor;

                if (aggregatedData[test_name] === undefined) {
                    aggregatedData[test_name] = []
                }
                aggregatedData[test_name].push({x: bm.num_models, y: bm.query_time_sql});
            });

            var rawData = [];
            $.each(aggregatedData, function(key, values) {
                rawData.push({
                    key: key,
                    values: values,
                });
            });

            nv.addGraph(function() {
              var chart = nv.models.lineWithFocusChart();

              chart.xAxis
                  .tickFormat(d3.format(',f'));
              chart.x2Axis
                  .tickFormat(d3.format(',f'));

              chart.yAxis
                  .tickFormat(d3.format(',.2f'));
              chart.y2Axis
                  .tickFormat(d3.format(',.2f'));

              d3.select("#canvas svg")
                  .datum(rawData)
                  .call(chart);

              nv.utils.windowResize(chart.update);

              return chart;
            });
        }
    });

})();
