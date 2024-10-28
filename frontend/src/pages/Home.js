import axios from 'axios'
import {useState} from 'react'
function Home(){
    const [inputValue,setInputValues]=useState('');
    const [response, setResponse]=useState('');
    
    const sendusername= async()=>{
        try{
            console.log(response.data)
            const res=await axios.post('http://localhost:3000/userfound',{
                content:inputValue,
            });
            setResponse(res.data.receive_content);
            console.log(setResponse)
        }catch(error){
            console.error('Error sending string',error)
        }
    };
    return(
        <div>
            <h1>Main page</h1>
            <input type="text" 
            value={inputValue} 
            onChange={(e)=> setInputValues(e.target.value)}/>
            <button onClick={sendusername}>검색</button>
            <p>Eternal Return</p>
        </div>
    );
}
export default Home;