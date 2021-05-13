// 左上
(function() {
    var chart = echarts.init(document.querySelector(".bar .chart"), 'white', {
        renderer: 'canvas'
    });
    $(
        function() {
            fetchData(chart);
            setInterval(fetchData, 2000);
        }
    );

    function fetchData() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/time_finish_Chart",
            dataType: 'json',
            success: function(result) {
                chart.setOption(result);
            }
        });
    }
})();


// 左中
(function() {
    var chart = echarts.init(document.querySelector(".line .chart"), 'white', {
        renderer: 'canvas'
    });
    $(
        function() {
            fetchData(chart);
            setInterval(fetchData, 2000);
        }
    );

    function fetchData() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/score_like_Chart",
            dataType: 'json',
            success: function(result) {
                chart.setOption(result);
            }
        });
    }
})();

// 左下
(function() {
    var chart = echarts.init(document.querySelector(".pie .chart"), 'white', {
        renderer: 'canvas'
    });
    $(
        function() {
            fetchData(chart);
            setInterval(fetchData, 2000);
        }
    );

    function fetchData() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/visitor_image_Chart",
            dataType: 'json',
            success: function(result) {
                chart.setOption(result);
            }
        });
    }
})();

// 热力图
(function() {
    var chart = echarts.init(document.querySelector(".bot1"), 'white', {
        renderer: 'canvas'
    });
    $(
        function() {
            fetchData(chart);
            setInterval(fetchData, 2000);
        }
    );

    function fetchData() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/funnel_top_Chart",
            dataType: 'json',
            success: function(result) {
                chart.setOption(result);
            }
        });
    }
})();

//右上

(function() {
    var chart = echarts.init(document.querySelector(".bar1 .chart"), 'white', {
        renderer: 'canvas'
    });
    $(
        function() {
            fetchData(chart);
            setInterval(fetchData, 200000);
        }
    );
    function fetchData() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/relation_like_Chart",
            dataType: 'json',
            success: function(result) {
                chart.setOption(result);
            }
        });
    }
})();

// 右中
(function() {
    var chart = echarts.init(document.querySelector(".line1 .chart"), 'white', {
        renderer: 'canvas'
    });
    $(
        function() {
            fetchData(chart);
            setInterval(fetchData, 2000);
        }
    );

    function fetchData() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/time_like_Chart",
            dataType: 'json',
            success: function(result) {
                chart.setOption(result);
            }
        });
    }
})();

//右下
(function() {
    var chart = echarts.init(document.querySelector(".pie1 .chart"), 'white', {
        renderer: 'canvas'
    });
    $(
        function() {
            fetchData(chart);
            setInterval(fetchData, 2000);
        }
    );

    function fetchData() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/tree_image_Chart",
            dataType: 'json',
            success: function(result) {
                chart.setOption(result);
            }
        });
    }
})();

// 中间底部
(function() {
    var chart = echarts.init(document.querySelector(".chart3"), 'white', {
        renderer: 'canvas'
    });
    $(
        function() {
            fetchData(chart);
            setInterval(fetchData, 2000);
        }
    );

    function fetchData() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/pie_many_Chart",
            dataType: 'json',
            success: function(result) {
                chart.setOption(result);
            }
        });
    }
})();