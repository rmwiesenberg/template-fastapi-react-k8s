import React from 'react'
import logo from './logo.svg'
import { doEcho } from './api'

function App() {
    const [echo, setEcho] = React.useState<string | undefined>(undefined)

    if (!echo) {
        doEcho({ msg: 'This came from the server!' }).then((value) => {
            setEcho(value?.msg)
        })
    }

    return (
        <div className="App">
            <header className="App-header">
                <p>
                    Edit <code>src/App.tsx</code> and save to reload.
                </p>
                <p>{echo ?? 'Waiting for echo...'}</p>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Learn React
                </a>
                <img src={logo} className="App-logo" alt="logo" />
            </header>
        </div>
    )
}

export default App
