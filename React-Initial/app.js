class App extends React.Component {
  render() {
    return (
      <div>
        <Hello />
        <Slot s1="x" s2="x" s3="x" />
        <Friend name="Elton" hobbies={["Piano", "Singing", "Dancing"]} />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
