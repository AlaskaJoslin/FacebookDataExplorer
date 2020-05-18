import React from 'react';
import ReactJson from 'react-json-view';
import './App.css';
import myData from './all_data.json';

function App() {
    // load in JSON data from file
    // var data;

    // var oReq = new XMLHttpRequest();
    // oReq.onload = reqListener;
    // oReq.open("get", "all_data.json", true);
    // oReq.send();

    // function reqListener(e) {
    //     data = JSON.parse(this.responseText);
    // }
    // var data = require('json!./all_data.json');

    // console.log(myData);


    return (
        <div className="App">
            <header className="App-header">
                <ReactJson src={myData} collapsed={true} theme="monokai" />
            </header>
        </div>
    );
}

export default App;
