import { useForm } from 'react-hook-form'
import { useNavigate } from 'react-router-dom'
import { authService } from '../../services'

const Login = () => {
  const { register, handleSubmit } = useForm()
  const navigate = useNavigate()

  const login = async (user) => {
    await authService.login(user)
    navigate('auto_parks')
  }

  return (
    <form onSubmit={handleSubmit(login)}>
      <input type="text" placeholder={'email'} {...register('email')}/>
      <input type="text" placeholder={''} {...register('password')}/>
      <button>login</button>
    </form>
  )
}

export { Login }