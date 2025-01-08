import axios from 'axios'
import React from 'react'
import {useState, useEffect} from 'react'
function Home(){         
    const [inputValue,setInputValue]=useState('');
    const [responseData, setResponseData]=useState('');
    const [resultdata,setResultData]=useState('');
    const [keylistData,setKeylistData]=useState('')
    
    useEffect(() => {
        console.log('Updated response:', responseData);
    }, [responseData]);

    const sendusername= async()=>{
        try{
            const res=await axios.post('http://localhost:3000/userfound',{
                content:inputValue,
            });
            // console.log(res)
            setResponseData(res.data)
            // console.log(res.data)
            // console.log(Object.keys(res.data).length)
            setKeylistData(Object.keys(res.data[0]))
            // console.log("233")
            // console.log(Object.keys(res.data[0])[1])
            resopen()
            // console.log(res)
        }catch(error){
            console.error('Error sending string',error)
        }
    };

    const resopen =()=>{
        console.log("resopen")
        const resdata=[];
        console.log(responseData[0])
        // console.log(Object.keys(response).length)
        for(let i=0; i < Object.keys(responseData).length;i++){
            // console.log("resopen1")
            console.log(responseData[i].gameId)
            for(let j=0;j<keylistData.length;j++){
                // console.log(i)
                // const key=keylist[j]
                // console.log(keylist[j])
                // console.log(response[i][keylist[j]])
                resdata.push(<span key={i}>{keylistData[j]+":"+responseData[i][keylistData[j]]+" ,"}</span>)
                }
                resdata.push(<br/>);
        }
        setResultData(resdata)
    };

    return(
        <div>
            <h1>Main page</h1>
            <input type="text" 
            value={inputValue} 
            onChange={(e)=> setInputValue(e.target.value)}/>
            <button onClick={sendusername}>검색</button>
            <div>{resultdata}</div>
            <p>Eternal Return</p>
        </div>
    );
}
export default Home;