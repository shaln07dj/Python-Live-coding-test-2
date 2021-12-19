const hello =()=>{ return new Promise((res,rej)=>{
    setTimeout(()=>{
       res(99)
    },5000)
  })
  }
  
  hello().then((resp)=>console.log(resp))