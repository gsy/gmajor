import React, { Component } from 'react'

import {Attributes} from './Attributes'
import {Direction} from './Direction'
import {Note} from './Note'

export default class Measure extends Component {
  render () {
    console.log("measure number:", this.props.number)
    return (
      <div>
        <Attributes />
        <Direction />
        <Note />
      </div>
    )
  }
}
