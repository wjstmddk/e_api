import {useState, useEffect} from 'react';


function Test(){
    const [data, setData]=useState([]);

    useEffect(()=>{
        fetch('http://localhost:3000/data')
        .then(response=>response.json())
        .then(data=>{
            console.log('data: ',data);
            setData(data)})
        .catch(error=>console.error('Error get data:',error));
}, []);

    return(
        <div>
            <h1>data view</h1>
            <p>dataList</p>
            <ul>
                {data.length>0? (  
                    data.map(item=>( 
                        <li key={item.id}>
                            ID:{item.id}, Status:{item.connect_status}
                        </li>
                    ))
                ):(
                    <p>data end</p>
                )}
            </ul>
        </div>
    );
}
export default Test;