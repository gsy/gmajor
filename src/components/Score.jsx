import React, { Component } from 'react'

import {Meta} from './Meta'
import Measure from './Measure'


export class Score extends Component {
  render() {
    return (
      <div>
        <Meta />
        <p>
          this is a score
        </p>
        <Measure number="1" />
      </div>
    )
  }
}
