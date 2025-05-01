




import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import { BubbleSort } from './pages/Bubble.Sort'
import { RecoilRoot } from 'recoil'

function App() {

  return (
    <Main/>
  )
}


function Main() {
    return (
      <RecoilRoot>
        <BrowserRouter>
          <Routes>
            <Route path='/bubble-sort' element={<BubbleSort/>}/>
          </Routes>
        </BrowserRouter>
      </RecoilRoot>
    )
}


export default App
