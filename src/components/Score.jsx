import React, { Component } from 'react'

import {Meta} from './Meta'
import {Measure} from './Measure'
import {GuitarMeasure} from './GuitarMeasure'
import {FlexLayout} from './Layout'


class FakeMeasure extends Component {
  /* 是要把 flex 里面的 layout 翻译成 svg 的坐标变换等 api */
  // 只有一个小节怎么处理？
  render () {
    const {number, layout, node, root} = this.props
    const transformation = `translate(${layout.layout.left},${layout.layout.top})`;
    return (
      <g transform={transformation}>
        <rect {...layout}
              fill="pink"
              stroke="pink"
              strokeWidth="5px"
              />
        <FlexLayout node={node}>
          <BeatBox key="11"/>
          <BeatBox key="21" />
        </FlexLayout>
      </g>
    )
  }
}

class BeatBox extends Component {
  render () {
    const {layout} = this.props
    const transformation = `translate(${layout.layout.left},${layout.layout.top})`;

    console.log("layout:", layout)
    return (
      <g transform={transformation}>
        <rect {...layout}
              fill="orange"
              stroke="orange"
              strokeWidth="5px"
              />
      </g>
    )
  }
}

export class Score extends Component {

  render() {
    const {doc} = this.props

    // if (doc == null) {
    //   return null
    // }

    // var measures = doc.getElementsByTagName("measure")
    // var measure = measures[0]

    // var noteElements = measure.getElementsByTagName("note")
    // var notes = []

    // for (var i=0; i<noteElements.length; i++) {
    //   var note = noteElements[i];
    //   var chordElements = note.getElementsByTagName("chord")
    //   var technicalElement = note.getElementsByTagName("technical")[0]
    //   var stringElements = technicalElement.getElementsByTagName("string")
    //   var fretElements = technicalElement.getElementsByTagName("fret")

    //   var chord = false
    //   var string = ""
    //   var fret = ""

    //   if (chordElements.length > 0) {
    //     chord = true
    //   }

    //   if (stringElements.length > 0 && fretElements.length > 0) {
    //     console.log("string element:", stringElements[0])
    //     string = stringElements[0].childNodes[0].nodeValue
    //     fret = fretElements[0].childNodes[0].nodeValue
    //   }

    //   notes.push({
    //     "chord": chord,
    //     "string": string,
    //     "fret": fret
    //   })
    // }

    return (
      <div>
        {/* <Meta /> */}
        <svg  xmlns="http://www.w3.org/2000/svg"
              width="1000" height="600" viewBox="0 0 1000 600">
          <FlexLayout width="1000" height="600" isRoot={true}>
            <FakeMeasure key="1" />
            <FakeMeasure key="2" />
            <FakeMeasure key="3" />
            <FakeMeasure key="4" />
            <FakeMeasure key="5" />
            <FakeMeasure key="6" />
          </FlexLayout>
        </svg>
      </div>
    )
  }
}
