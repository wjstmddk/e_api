import React, {useState} from 'react';
import axios from 'axios'

function SendData(){
    const [formData,setFormData]=useState({
        connect_status: 0,
    }); 

    const handleInputChange=(e)=>{
        const name= String(e.target.name);
        const value=e.target.value;
        setFormData({
            ...formData,
            [name]: parseInt(value,10),    
        });
    };

    const handleSubmit=(e)=>{
        e.preventDefault();
        // console.log(formData)
        // console.log(typeof(formData.connect_status))
        // console.log(typeof(Object.keys(formData)))
        // console.log(Object.keys(formData))
        axios.post('http://localhost:3000/getdata',formData,{
            // transformRequest:[(data,headers)=>{
            //     return data;
            // }],
            headers:{'Context-Type': 'application/json'}
        })
            .then((response)=>{
                console.log('Success:', response.data);
            })
            .catch((error)=>{
                console.error('Error:',error);
            });
    };

    return(
        <form onSubmit={handleSubmit}>
            <input type="number" name='connect_status'value={formData.connect_status||0} onChange={handleInputChange} placeholder='number'/>
            <button type="submit">submit</button>
        </form>
    );
} 
export default SendData;