const ctx = document.getElementById('chart')

new Chart(
    ctx,{
        type:'bar',
        data:{
            labels:['python','java','php','golang'],
            datasets:[
                {
                    data:[10,50,47,36],
                    label:'Custom Text Now',
                }
            ],     
        },
        options:{
            responsive:false,
        }

    }
)