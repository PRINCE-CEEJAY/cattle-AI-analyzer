import { createRoot } from 'react-dom/client'
import { BrowserRouter as Router } from 'react-router-dom'
import './index.css'
import App from './App.jsx'
import Sidebar from "./components/SideBar"

createRoot(document.getElementById('root')).render(
  <div className='flex min-h-screen'> 
  <Router>
      <Sidebar/>
      <App />
  </Router>
  </div> 
)
