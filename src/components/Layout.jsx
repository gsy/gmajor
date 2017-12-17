import React, { Component } from 'react'
import yoga, { Node } from 'yoga-layout'

export class FlexLayout extends Component {

  render () {
    const {width, height, padding, children, content, isRoot} = this.props
    console.log("width:", width)
    console.log("height:", height)

    var node = Node.create()
    node.setWidth(width)
    node.setHeight(height)
    node.setPadding(yoga.EDGE_ALL, padding)
    node.setDisplay(yoga.DISPLAY_FLEX)
    node.setFlexDirection(yoga.FLEX_DIRECTION_ROW)

    if (children && children.length > 0) {
      for (var i=0; i <children.length; i++) {
        node.insertChild(children[i])
      }
    }

    /* left to right */
    if (isRoot) {
      node.calculateLayout(width, height, yoga.DIRECTION_LTR)
    }

    return (
      {content}
    )
  }
}
