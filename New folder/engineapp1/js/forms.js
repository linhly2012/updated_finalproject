$(document).ready(function() {
    // var x = document.getElementById("mynetwork").value;
    // console.log(x);
    myList = [];
    function createNodes(list) {
      tempNodes = [];
      tempDicNodes = {};
      for (i = 1; i <= list.length; i += 1) {
        tempNodes.push({id: i, label: list[i-1]});
      }

      //nested for loops because there are multiple dictionaries inside of one list

      console.log(tempDicNodes);
      console.log(tempNodes);
      var nodes = new vis.DataSet(tempNodes);
      //     {id: 1, label: name},
      //     {id: 2, label: name2}
      // ]);

      tempEdges = [];
      tempDicEdges = {};
      for (i = 1; i < list.length; i += 1) {
        tempEdges.push({from: i, to: i+1})
        // tempDicEdges['from']=[i];
        // tempDicEdges['to']=[i+1];
      }

      tempEdges.push(tempDicEdges);
      console.log(tempEdges);
      console.log(tempDicEdges);
      // create an array with edges
      var edges = new vis.DataSet(tempEdges);
      //     {from: 1, to: 2}
      // ]);


      // create a network
      var container = document.getElementById('mynetwork');

      // provide the data in the vis format
      var data = {
          nodes: nodes,
          edges: edges
      };

      //CSS properties of the nodes
      var options = {
        nodes: {
          borderWidth: 3,
          shape: 'circle'
        },
        autoResize: false,



        // interaction: {
        //   navigationButtons: true
        // }
      };

      // initialize your network!
      var network = new vis.Network(container, data, options);
      network.setSize('100%', '100%');
      network.navigationButtons = true;
      // container = document.getElementById('mynetwork');



    }

    $('#submitButton').click(function() {
      var name = $('#first').val();
      //var name2 = $('#second').val();
      name = name.toUpperCase();
      $('#first').val('');
      //$('#second').val(name2);
      myList.push(name);

      $("#first").focus();
      window.location.hash = '#mynetwork';
      //$('submitButton').focus();

      //myList.push(name2);
      createNodes(myList)

        });

    })
