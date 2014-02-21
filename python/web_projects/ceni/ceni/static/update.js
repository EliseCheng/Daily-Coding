 var values = [];
        for (var i=0; i<150; i++){
            values[i] = i + "";
        }
  	var cpu_data = {
			fillColor : "rgba(153,204,153,0.3)",
			strokeColor : "rgba(153,204,0,1)",
			pointColor : "rgba(220,220,220,1)",
			pointStrokeColor : "#fff",
			data : values//[65,59,90,81,56,55,40]
		};
	var mem_data = {
			fillColor : "rgba(255,204,204,0.3)",
			strokeColor : "rgba(204,0,51,1)",
			pointColor : "rgba(220,220,220,1)",
			pointStrokeColor : "#fff",
			data : values//[65,59,90,81,56,55,40]
		};   
	var data = {
			fillColor : "rgba(255,255,255,0)",
			strokeColor : "rgba(255,255,255,0)",
			pointColor : "rgba(255,255,255,0)",
			pointStrokeColor : "#fff",
			data : values//[65,59,90,81,56,55,40]
		}; 
	var lineChartData = {
		labels : values,//["0","","March","April","May","June","July"],
		datasets : [
				data
			]
		}
	var initChartData = lineChartData;
	var ctx = document.getElementById("myChart").getContext("2d");
	var myNewChart = new Chart(ctx).Line(lineChartData);
       
	var dev_data = {};
	var timer;
	function getVal(dev_data){       
            values.shift();
            values.push(Math.floor(Math.random() * (80 - 60) + 60));
            //lineChartData["datasets"][0]["data"] = values;
	    dev_data["data"] = values;
	    lineChartData["datasets"] = [ dev_data ];
            new Chart(document.getElementById("myChart").getContext("2d")).Line(lineChartData);
            timer = setTimeout(function(){ getVal(dev_data) },1000);
  }
	function initChart(){
		new Chart(document.getElementById("myChart").getContext("2d")).Line(initChartData);
	}

	function change(dev){
		switch(dev){
			case 1:
				clearTimeout(timer);
				initChart();
				getVal(cpu_data);				
			break;
			case 2:
				clearTimeout(timer);
				initChart();
				getVal(mem_data);
			break;
		}
	}
