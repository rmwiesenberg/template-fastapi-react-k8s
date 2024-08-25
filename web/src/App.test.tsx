import renderer from 'react-test-renderer'
import App from './App'

it('app renders at all', () => {
    renderer.create(
        <App />,
    )
})
