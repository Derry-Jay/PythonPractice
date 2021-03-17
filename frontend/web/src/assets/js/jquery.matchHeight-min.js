/**
* jquery.matchHeight-min.js master
* http://brm.io/jquery-match-height/
* License: MIT
*/
(function (c) {
  var n = -1, f = -1, g = function (a) { return parseFloat(a) || 0 }, r = function (a) { var b = null, d = []; c(a).each(function () { var a = c(this), k = a.offset().top - g(a.css('margin-top')), l = d.length > 0 ? d[d.length - 1] : null; l === null ? d.push(a) : Math.floor(Math.abs(b - k)) <= 1 ? d[d.length - 1] = l.add(a) : d.push(a); b = k }); return d }, p = function (a) { var b = { byRow: !0, property: 'height', target: null, remove: !1 }; if (typeof a === 'object') return c.extend(b, a); typeof a === 'boolean' ? b.byRow = a : a === 'remove' && (b.remove = !0); return b }, b = c.fn.matchHeight =
        function (a) { a = p(a); if (a.remove) { var e = this; this.css(a.property, ''); c.each(b._groups, function (a, b) { b.elements = b.elements.not(e) }); return this } if (this.length <= 1 && !a.target) return this; b._groups.push({ elements: this, options: a }); b._apply(this, a); return this }; b._groups = []; b._throttle = 80; b._maintainScroll = !1; b._beforeUpdate = null; b._afterUpdate = null; b._apply = function (a, e) {
    var d = p(e), h = c(a), k = [h], l = c(window).scrollTop(), f = c('html').outerHeight(!0), m = h.parents().filter(':hidden'); m.each(function () {
      var a = c(this)
      a.data('style-cache', a.attr('style'))
    }); m.css('display', 'block'); d.byRow && !d.target && (h.each(function () { var a = c(this), b = a.css('display'); b !== 'inline-block' && b !== 'inline-flex' && (b = 'block'); a.data('style-cache', a.attr('style')); a.css({ display: b, 'padding-top': '0', 'padding-bottom': '0', 'margin-top': '0', 'margin-bottom': '0', 'border-top-width': '0', 'border-bottom-width': '0', height: '100px' }) }), k = r(h), h.each(function () { var a = c(this); a.attr('style', a.data('style-cache') || '') })); c.each(k, function (a, b) {
      var e = c(b),
        f = 0; if (d.target) f = d.target.outerHeight(!1); else { if (d.byRow && e.length <= 1) { e.css(d.property, ''); return } e.each(function () { var a = c(this), b = a.css('display'); b !== 'inline-block' && b !== 'inline-flex' && (b = 'block'); b = { display: b }; b[d.property] = ''; a.css(b); a.outerHeight(!1) > f && (f = a.outerHeight(!1)); a.css('display', '') }) } e.each(function () {
        var a = c(this), b = 0; d.target && a.is(d.target) || (a.css('box-sizing') !== 'border-box' && (b += g(a.css('border-top-width')) + g(a.css('border-bottom-width')), b += g(a.css('padding-top')) + g(a.css('padding-bottom'))),
        a.css(d.property, f - b + 'px'))
      })
    }); m.each(function () { var a = c(this); a.attr('style', a.data('style-cache') || null) }); b._maintainScroll && c(window).scrollTop(l / f * c('html').outerHeight(!0)); return this
  }; b._applyDataApi = function () { var a = {}; c('[data-match-height], [data-mh]').each(function () { var b = c(this), d = b.attr('data-mh') || b.attr('data-match-height'); a[d] = d in a ? a[d].add(b) : b }); c.each(a, function () { this.matchHeight(!0) }) }; var q = function (a) {
    b._beforeUpdate && b._beforeUpdate(a, b._groups); c.each(b._groups, function () {
      b._apply(this.elements,
        this.options)
    }); b._afterUpdate && b._afterUpdate(a, b._groups)
  }; b._update = function (a, e) { if (e && e.type === 'resize') { var d = c(window).width(); if (d === n) return; n = d } a ? f === -1 && (f = setTimeout(function () { q(e); f = -1 }, b._throttle)) : q(e) }; c(b._applyDataApi); c(window).bind('load', function (a) { b._update(!1, a) }); c(window).bind('resize orientationchange', function (a) { b._update(!0, a) })
})(jQuery)
