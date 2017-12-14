import React, { Component } from 'react'

export class Note extends Component {
  /* 根据类型找到 head 的 codepoint */
  getHeadCode(type) {
    switch (type) {
      case 'whole':
        /* noteheadHalf */
        return '\uE0A3'
      case 'quarter':
      case 'eight':
        /* noteheadBlack */
        return '\uE0A4';
    }
  }

  /* stem 的 unicode codepoint */
  getStemCode() {
    return '\uE210';
  }

  render () {
    var pitch = 'c4';/* 用来定音高 */
    var duration = 1;/*  */
    var type = 'eight';/* 8分音符 */
    var stem = 'down';/* 向上 */
    /* technical */
    var string = '2';
    var fret = '1';

    var headCode = this.getHeadCode(type);
    var stemCode = this.getStemCode();

    switch (stem) {
      case 'up':
        return (
        <div className="Element">
          <span>{headCode}</span>
          <span className="left up-a-bit">{stemCode}</span>
        </div>
      )
      case 'down':
      return (
        <div className="Element relative-align">
          <span className="border">{stemCode}</span>
          <span className="border left up-total">{headCode}</span>
        </div>
      )
    }
  }
}
