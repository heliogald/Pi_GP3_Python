(function(win,doc){
    'use strict';

    doc.querySelector('.btn').addEventListener('click',async(event)=>{
        event.preventDefault();
        let req=await fetch('http://localhost:8000/pesquisas/filtrarPais/',{
            method:'POST',
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json',
                'X-CSRFToken':doc.querySelectorAll('input')[0].value
            },
            body:JSON.stringify({
                'country':doc.querySelector('#country').value,
                'Match':doc.querySelector('#Match').value,
            })
        });
        let res=await req.json();
        doc.querySelector('.result').innerHTML=res.data;
    },false);

})(window,document);