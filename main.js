document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{const id=a.getAttribute('href');const el=document.querySelector(id);if(el){e.preventDefault();el.scrollIntoView({behavior:'smooth'});}}));

const testimonials=[...document.querySelectorAll('.testimonial')];
const dots=[...document.querySelectorAll('.testimonial-dot')];
let testimonialIndex=0;
function showTestimonial(index){
  if(!testimonials.length) return;
  testimonialIndex=(index+testimonials.length)%testimonials.length;
  testimonials.forEach((t,i)=>t.classList.toggle('active',i===testimonialIndex));
  dots.forEach((d,i)=>d.classList.toggle('active',i===testimonialIndex));
}
dots.forEach((dot,i)=>dot.addEventListener('click',()=>showTestimonial(i)));
if(testimonials.length){setInterval(()=>showTestimonial(testimonialIndex+1),5000);}
