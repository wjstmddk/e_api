import axios from 'axios'
import {useState} from 'react'
function Home(){
    const [inputValue,setInputValues]=useState('');
    const [response, setResponse]=useState('');
    
    const sendusername= async()=>{
        try{
            const res=await axios.post('http://localhost:3000/userfound',{
                content:inputValue,
            });
            console.log(response)
            setResponse(res.data.receive_content);
            console.log(response)
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
            <div>
                <p>{response}</p>
            </div>
            <p>Eternal Return</p>
        </div>
    );
}
export default Home;