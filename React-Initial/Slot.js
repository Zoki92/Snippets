class Slot extends React.Component {
  render() {
    const { s1, s2, s3 } = this.props;
    const winner = s1 === s2 && s2 === s3;
    return (
      <div>
        <p>
          {s1} {s2} {s3}
        </p>

        <h1>{winner ? "Winner!" : "Loser"}</h1>
      </div>
    );
  }
}

ReactDOM.render(<Slot />, document.getElementById("root"));
