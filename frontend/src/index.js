import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './Router/Router';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { SpeedInsights } from "@vercel/speed-insights/react"
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
reportWebVitals();
