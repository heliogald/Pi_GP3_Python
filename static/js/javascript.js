(function(win,doc){
    'use strict';

    doc.querySelector('.btn').addEventListener('click',async(event)=>{
        event.preventDefault();
        let req=await fetch('http://localhost:8000/pesquisas/consultarPesquisa/',{
            method:'POST',
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json',
                'X-CSRFToken':doc.querySelectorAll('input')[0].value
            },
            body:JSON.stringify({
                'country':doc.querySelector('#country').value,
                'title':doc.querySelector('#title').value,
            })
        });
        let res=await req.json();
        doc.querySelector('.result').innerHTML=res.data;
    },false);

})(window,document);