import React, { Component } from 'react'

export class Note extends Component {
  render () {
    console.log("props:", this.props)
    return (
      <div className="Element">
        <code>&#xE262;&#xE0A4;</code>
        This is one note
      </div>
    )
  }
}
