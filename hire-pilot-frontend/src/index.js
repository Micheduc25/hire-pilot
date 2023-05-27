import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './index.css';
import App from './App';
import DashboardEmployer from './DashboardEmployer/DashboardEmployer';
import Layout from './Layout/layout';
import ApplyForm from './Apply/ApplyForm';
import Status from './Status/Status';
import AllJobs  from './Tables/AllJobs';


export default function Appp() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<Layout />}>
        <Route index element={<App />} />
        <Route path='dashboardemployer' element={<DashboardEmployer />} />
        <Route path='apply' element={<ApplyForm />} />
        <Route path='status' element={<Status />} />
        <Route path='alljobs' element={<AllJobs />} />



      </Route>
    </Routes>
    </BrowserRouter>
  );
}

ReactDOM.render(<Appp />, document.getElementById('root'));
