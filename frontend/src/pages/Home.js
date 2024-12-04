import axios from 'axios'
import React from 'react'
import {useState, useEffect} from 'react'
function Home(){
    const [inputValue,setInputValue]=useState('');
    const [response, setResponse]=useState('');
    
    useEffect(() => {
        console.log('Updated response:', response);
    }, [response]);

    const sendusername= async()=>{
        try{
            const res=await axios.post('http://localhost:3000/userfound',{
                content:inputValue,
            });
            // console.log(res)
            setResponse(res.data)
            // console.log(res.data)
            // console.log(res)
        }catch(error){
            console.error('Error sending string',error)
        }
    };

    return(
        <div>
            <h1>Main page</h1>
            <input type="text" 
            value={inputValue} 
            onChange={(e)=> setInputValue(e.target.value)}/>
            <button onClick={sendusername}>검색</button>
            <div>
                <p>{response}</p>
            </div>
            <p>Eternal Return</p>
        </div>
    );
}
export default Home;