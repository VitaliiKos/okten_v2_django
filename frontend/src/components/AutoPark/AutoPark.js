const AutoPark = ({autoPark}) => {
  const { id, name } = autoPark
  return (
    <div>
      <div>id: {id}</div>
      <div>name: {name}</div>
    </div>
  )
}

export { AutoPark }