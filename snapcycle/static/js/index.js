window.onload =()=>{
   /* /* const transition_el = document.querySelector('.transition');
    const anchors= document.querySelectorAll('a');
    setTimeout(()=> {
        transition_el.classList.remove('is-active');
    },500);

    for(let i=0; i<anchors.length;i++){
        const anchor= anchors[i];

        anchor.addEventListener('click', e=>{
            e.preventDefault(); // not linking to diff page
            let target= e.target.href;

            transition_el.classList.add('is-active');
            setTimeout(()=>{
                window.location.href = target;
            },500)
        })
    }*/
    const btn = document.querySelector('.contactbtn');
    const elems = document.querySelectorAll('.transition');
    btn.addEventListener('click', e=>{
        for(let i=0; i<elems.length;i++){
        const elem= elems[i];
            console.log('here')
            setTimeout(()=>{
                elem.classList.toggle('is-active');
            },500)
            
            }
        })
    const contactsection = document.querySelector('.contact');
    contactsection.addEventListener('click', e=>{
        for(let i=0; i<elems.length;i++){
            const elem= elems[i];
                console.log('here')
                setTimeout(()=>{
                    elem.classList.toggle('is-active');
                },500)
                
                }
            })
}