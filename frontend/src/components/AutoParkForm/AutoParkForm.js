import { useForm } from 'react-hook-form'
import { autoParkService } from '../../services'

const AutoParkForm = ({setAutoParks}) => {
  const { register, handleSubmit, reset } = useForm()
  const save = async (autoPark) => {
    const { data } = await autoParkService.create(autoPark)
    setAutoParks(prev=>[...prev, data])
    reset()
  }
  return (
    <form onSubmit={handleSubmit(save)}>
      <input type="text" placeholder={''} {...register('name')}/>
      <button>Save</button>
    </form>
  )
}

export { AutoParkForm }