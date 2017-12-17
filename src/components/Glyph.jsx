import React, { Component } from 'react'

export class Glyph extends Component {
  render () {
    const {x, y, width, height, codePoint, fontSize, id} = this.props
    var code = String.fromCharCode(parseInt(codePoint, 16))

    return (
      <g>
      <rect x={x} y={y} width={width} height={height} fill="red"></rect>
      <text id={"tspan" + id} x={x} y={y} fontSize={fontSize.toString()} fontFamily="Bravura">
          {code}
      </text>
      </g>
    )
  }
}
