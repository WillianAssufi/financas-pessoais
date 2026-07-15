import { useState } from "react"
import { useNavigate } from "react-router-dom"

function Login({ onLogin }) {
    const [email, setEmail] = useState('')
    const [senha, setSenha] = useState('')
    const [error, setError] = useState('')
    const navigate = useNavigate()

    async function handleLogin() {

        const response = await fetch('http://localhost:8000/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: `username=${email}&password=${senha}`
        })
        console.log(response)
        const dados = await response.json()
        if (dados.detail) {
            setError(dados.detail)
            return
        }
        console.log(dados)
        onLogin(dados.access_token)
        navigate('/dashboard')
    }

    return (
        <div>
            <label htmlFor="email">Email: </label>
            <p>
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Digite seu Email aqui..." />
            </p>
            <label htmlFor="senha">Senha:</label>
            <p>
                <input type="password" value={senha} onChange={(e) => setSenha(e.target.value)} placeholder="Digite sua Senha aqui..." />
            </p>
            <button onClick={handleLogin}>Login</button>
            {error && (<p>{error}</p>)}
        </div>

    )
}

export default Login