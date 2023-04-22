import { Route, Routes } from 'react-router-dom'

import { AutoParks, Login } from './components'

const App = () => {
  return (
    <div>
      <Routes>
        <Route path={'/'} element={<Login/>}/>
        <Route path={'auto_parks'} element={<AutoParks/>}/>
      </Routes>
    </div>
  )
}

export { App }