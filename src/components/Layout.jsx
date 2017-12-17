import React, { Component } from 'react'
import yoga, { Node } from 'yoga-layout'

export class FlexLayout extends Component {
  render () {
    const width = this.props.width || yoga.UNDEFINED
    const height = this.props.height || yoga.UNDEFINED

    var root = Node.create()
    root.setDisplay(yoga.DISPLAY_FLEX)
    root.setWidth(width)
    root.setHeight(height)
    root.setFlexDirection(yoga.FLEX_DIRECTION_ROW)
    root.setJustifyContent(yoga.JUSTIFY_FLEX_START)
    root.setFlexWrap(yoga.WRAP_WRAP)

    /* parse child style，拿出跟 flexbox 有关的信息，换成 node 的 api */
    this.props.children.map((child, index) => {
      var childNode = Node.create();
      childNode.setWidth("30%");
      childNode.setHeight(100);
      childNode.setMargin(yoga.EDGE_ALL, 10)
      root.insertChild(childNode, index);
    })

    root.calculateLayout(width, height, yoga.DIRECTION_LTR)

    var layoutMapping = {}
    this.props.children.map((child, index) => {
      let childNode = root.getChild(index);
      const layout = {
        "layout": childNode.getComputedLayout(),
        "width": childNode.getComputedWidth(),
        "height": childNode.getComputedHeight()
      }
      layoutMapping[child.key] = layout
    })

    const childrenWithLayout = React.Children.map(this.props.children, (child) => React.cloneElement(child, { layout: layoutMapping[child.key] }))

    return childrenWithLayout
  }
}
