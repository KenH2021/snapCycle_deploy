const swup = new Swup();

// window.onload = () => {
//     /* /* const transition_el = document.querySelector('.transition');
//      const anchors= document.querySelectorAll('a');
//      setTimeout(()=> {
//          transition_el.classList.remove('is-active');
//      },500);
 
//      for(let i=0; i<anchors.length;i++){
//          const anchor= anchors[i];
 
//          anchor.addEventListener('click', e=>{
//              e.preventDefault(); // not linking to diff page
//              let target= e.target.href;
 
//              transition_el.classList.add('is-active');
//              setTimeout(()=>{
//                  window.location.href = target;
//              },500)
//          })
//      }*/
//     const contactbtn = document.querySelector('.contactbtn');
//     const proposbtn = document.querySelector('.proposbtn');
//     const elems2 = document.querySelectorAll('.transition-2');
//     const elems3 = document.querySelectorAll('.transition-3');
//     contactbtn.addEventListener('click', e => {
//         for (let i = 0; i < elems2.length; i++) {
//             const elem = elems2[i];
//             console.log('here')
//             setTimeout(() => {
//                 elem.classList.toggle('is-active');
//             }, 500)

//         }
//     })

//     proposbtn.addEventListener('click', e => {
//         for (let i = 0; i < elems3.length; i++) {
//             const elem = elems3[i];
//             console.log('here')
//             setTimeout(() => {
//                 elem.classList.toggle('is-active');
//             }, 500)

//         }
//     })
//     const contactsection = document.querySelector('.contact');
//     contactsection.addEventListener('click', e => {
//         for (let i = 0; i < elems2.length; i++) {
//             const elem = elems2[i];
//             console.log('here')
//             setTimeout(() => {
//                 elem.classList.toggle('is-active');
//             }, 500)

//         }
//     })
//     const propossection = document.querySelector('.a-propos');
//     propossection.addEventListener('click', e => {
//         for (let i = 0; i < elems3.length; i++) {
//             const elem = elems3[i];
//             console.log('here')
//             setTimeout(() => {
//                 elem.classList.toggle('is-active');
//             }, 500)

//         }
//     })
// }