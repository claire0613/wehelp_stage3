const submitBtn=document.querySelector('#submit')
const uploadForm=document.querySelector('#upload-form')
const section=document.querySelector('section')
const uploadUrl='api/upload'
let main = document.querySelector('main');
async function load(){
    section.innerHTML=''
    const response=await fetch(uploadUrl)
    const promise=await response.json();
    const results=await promise;
   
    if (results.data){
        let reverseData=results.data.reverse()
        reverseData.forEach(ele => {
            const messageDiv=document.createElement('div')
            messageDiv.classList.add('msg-div')
            const messageText=document.createElement('p')
            messageText.innerHTML=ele["message"]
            const image=document.createElement('img')
            image.src=ele["image_url"]
            image.alt='upload pic'
            messageDiv.append(messageText,image)
            section.append(messageDiv)
        });
    }


}
load();


uploadForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    const formData = new FormData();
    const messageValue=uploadForm.querySelector('#message').value
    const pictureValue=uploadForm.querySelector('#image').files[0]
    formData.append('message',messageValue);
    formData.append('file',pictureValue);

    const option={
    method: 'POST',
    body:formData

    }

    fetch(uploadUrl,option)
    .then(res=>res.json())
    .then(data=>{
       
        load();
    })

    // const response=await fetch(uploadUrl,option)
    // const promise=await response.json();
    // const result=await promise;
    
})
