import './App.css';
import Dashboard from './components/Dashboard';
import SignIn from './components/SignIn';
import { BrowserRouter,Routes, Route} from "react-router-dom"
import SignUp from './components/SignUp';
import ForgetPassword from './components/ForgetPassword';


function App() {
  // const [token, setToken] = useState(null)
  
  return (
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<SignIn/>}/>
      <Route path='/signup' element={<SignUp/>}/>
      <Route path='/dashboard' element={<Dashboard/>}/>
      <Route path='/forgetpassword' element={<ForgetPassword/>}/>
    </Routes>
    </BrowserRouter>
  );
}

export default App;
