import axios from 'axios'
import React from 'react'
import {useState, useEffect} from 'react'
function Home(){         
    const [inputValue,setInputValue]=useState('');
    const [response, setResponse]=useState('');
    const [resdata,setResdata]=useState('');
    const [keylist,setKeylist]=useState('')
    
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
            // console.log(Object.keys(res.data).length)
            setKeylist(Object.keys(res.data[0])[0])
            // console.log("233")
            resopen()
            // console.log(res)
        }catch(error){
            console.error('Error sending string',error)
        }
    };

    const resopen =()=>{
        console.log("resopen")
        const resdata=[];
        console.log(response[0])
        // console.log(Object.keys(response).length)
        for(let i=0; i < Object.keys(response).length;i++){
            console.log("resopen1")
            const resjson=JSON.stringify(response[i])
            console.log(resjson.length)
            for(let j=0;j<Object.keys(resjson.length);j++){
                console.log(i)
                let keydata=Object.keys(resjson)
                console.log(keydata[1][0])
                resdata.push(<span key={i}>{resjson.keydata[i]+"/"}</span>)
                }
        }
        setResdata(resdata)
    };

    return(
        <div>
            <h1>Main page</h1>
            <input type="text" 
            value={inputValue} 
            onChange={(e)=> setInputValue(e.target.value)}/>
            <button onClick={sendusername}>검색</button>
            {/* <button onClick={resopen()}>결과확인</button> */}
            <div>{resdata}</div>
            <p>Eternal Return</p>
        </div>
    );
}
export default Home;