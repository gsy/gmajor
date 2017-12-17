import React, { Component } from 'react'

import {Meta} from './Meta'
import {Measure} from './Measure'
import {GuitarMeasure} from './GuitarMeasure'
import {FlexLayout} from './Layout'

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
        <Meta />
        <GuitarMeasure />

        <FlexLayout width="600" height="600" flex="row-wrap flex-start">
          <Measures />
        </FlexLayout>

      </div>
    )
  }
}
