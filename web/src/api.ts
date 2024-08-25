import { MyModel } from './model'
import axios from 'axios'

const url: URL = new URL(
    process.env.REACT_APP_API_URL ?? 'https://api.template.com',
)

const instance = axios.create({
    baseURL: url.toString(),
    timeout: 1000,
})

export const doEcho = async (msg: MyModel): Promise<MyModel | undefined> => {
    try {
        const response = await instance.post('/echo', msg)
        return response.data
    } catch (error) {
        console.log(error)
        return
    }
}
