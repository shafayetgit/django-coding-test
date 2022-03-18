import React from "react";
import ReactDOM from "react-dom";
import CreateProduct from "./components/CreateProduct";
import UpdateProduct from "./components/UpdateProduct";

// require('./bootstrap');
// require('./sb-admin');

const propsContainer = document.getElementById("variants");
const props = Object.assign({}, propsContainer.dataset);
if (props.variants == 'True'){
    const propsContainer = document.getElementById("variants");
    const props = Object.assign({}, propsContainer.dataset);

    ReactDOM.render(
        <React.StrictMode>
            <UpdateProduct {...props}/>
        </React.StrictMode>,
        document.getElementById('root')
    );
}else{
    ReactDOM.render(
        <React.StrictMode>
            <CreateProduct {...props}/>
        </React.StrictMode>,
        document.getElementById('root')
    );
}


