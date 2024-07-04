const ctx = document.getElementById('myChart');

new Chart(ctx,{
        // type:'doughnut',
        type:'bar',
        data:{
            labels:['python','javascript','php','java','django'],
            datasets: [{
                'data':[10,20,43,11,68],
                'label':'Programming Language',
                'backgroundColor':['red','black','green','lime','brown'],
                'borderColor':['green','red','white','black','blue'],
                'borderWidth':3,


            }]
        },
        options:{
            responsive:false, //to make width and height work.
            
            onClick:function(){
                alert('Sticks clicked');
                },
                
            animation: {
                  duration: 1000,
                  easing: 'easeInOutBounce',
                  //loop:true,        // use to make animation continuosly
                },

            layout:{
                padding:{
                    left:50,
                    top:100,
                    bottom:60,
                    },
                },
                

            plugins:{

                legend:{        //label hota h ye jo dataset me diya tha
                    display:true,
                    position:'top',

                    onHover: function(){
                        alert('hovering on legend');
                    },

                    labels:{
                        color:'green',
                        font:{
                            size:20,
                            style:'italic',
                            family:'Comic Sans MS',
                            },
                        boxWidth:200,
                    }
                },

                title:{
                    display:true,
                    text:'Custom Title',
                    position:'bottom',
                    color:'red',
                    font:{
                        family:'Comic Sans MS',
                        style:'italic',
                        size:50,
                    }
                },

                tooltip:{
                    enabled:true,
                    backgroundColor:'red',
                    titleColor:'black',             //use to color the title
                    titleAlign:'center',        // use to align title text {left,ight,center}
                    
                    titleFont:{
                        size:30,
                        style:'italic',
                        family:'Comic Sans MS',
                    },

                    bodyColor:'white',
                    bodyFont:{
                        size:20,
                        style:'underline',
                        family: 'Sarif',
                    },
                    position:'nearest',
                    xAlign:'left',      // it position the tooltip {left,right,center}
                    yAlign:'top',       //it position the tooltip on y axis{top,bottom,center}
                    
                    footerColor:'white',
                
                        },  

                    }
                
            },


    }
)