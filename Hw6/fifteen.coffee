#	> File Name: fifteen.coffee
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Thursday, December 18, 2014 AM09:45:50 CST

class Piece
    ###
    * the part of maze, a maze is expecting to have 15 pieces
    * @param col: the column position of piece
    * @param row: the row position of piece
    * @param id: the number of the piece, used as an identity(one and only)
    * @param element: the element belong to specific piece in DOM tree
    ###
    constructor: (@col, @row, @id, @element)->

class Maze
    ###
    * maze, which would encapsulate some essential methods
    * @param pieces: the array that contain all of the piece in maze
    * @param blankCol: recording the column position of blank in maze
    * @param @blankRow: recording the row position of blank in maze
    ###
    constructor: (@pieces = [], @blankCol = 4, @blankRow = 4)->

    ###
    * push a piece into pieces array
    * @param piece: the piece to push(class Piece)
    ###
    push: (piece)->
        @pieces.push piece

    ###
    * initialize maze
    * initialize dataStructure
    * initialize DOM element
    * add event listener for events
    ###
    initialize: ->
        @initializeDataStructure()
        @initializePieceElement()
        @updatePosition()
        that = @
        document.getElementById('shufflebutton').addEventListener 'click', ->
            that.shuffle(that)
        ele = document.getElementById('background-image')
        ele.onchange = ->
            that.changeBackground(ele)

    ###
    * initialize dataStructure of maze
    * for each step in loop, create a piece(class Piece), and push to pieces
    * add event handler to piece
    ###
    initializeDataStructure: ->
        col = 1
        pieces = document.getElementById('puzzlearea').getElementsByTagName 'div'
        while col < 5
            row = 1
            while row < 5
                piece = new Piece col, row, (col - 1) * 4 + row, pieces[(col - 1) * 4 + row - 1]
                if piece.element isnt undefined
                    @push piece
                    onePiece = @pieces[(col - 1) * 4 + row - 1]
                    that = @
                    ele = onePiece.element
                    ###
                    * in order to let all DOM element binding to their own piece, use a closure
                    * 'that' is maze, so that the function pieceClickHandler could execute in maze's action scope
                    * @param ele: the DOM element for piece
                    ###
                    onePiece.element.onclick = do (ele)->
                        ->
                            that.pieceClickHandler(ele)
                row++
            col++

    ###
    * initialize DOM element for piece
    ###
    initializePieceElement: ->
        for piece in @pieces
            if piece.element isnt undefined
                piece.element.style.backgroundPosition = -(piece.row - 1) * 100 + "px " + -(piece.col - 1) * 100 + "px"

    ###
    * update exactly where piece is in browser(syncing data and view)
    ###
    updatePosition: ->
        for piece in @pieces
            if piece.element isnt undefined
                piece.element.style.left = (piece.row - 1) * 100 + "px"
                piece.element.style.top = (piece.col - 1) * 100 + "px"
                if Math.abs(piece.row - @blankRow) + Math.abs(piece.col - @blankCol) > 1
                    piece.element.className = 'puzzlepiece'
                else
                    piece.element.className = 'puzzlepiece movablepiece'

    ###
    * event handler for click event for piece in maze
    * @param ele: the DOM element for piece
    ###
    pieceClickHandler: (ele)->
        index = parseInt ele.textContent
        if Math.abs(@pieces[index - 1].row - @blankRow) + Math.abs(@pieces[index - 1].col - @blankCol) <= 1
            @move index
            @updatePosition()
            if @completed()
                alert 'You Win!'

    ###
    * exchange pieces[index - 1] position data with blank position
    * @param index: recording which piece to exchange, stand for the postion(index - 1) in pieces array
    ###
    move: (index)->
        @pieces[index - 1].col ^= @blankCol
        @blankCol ^= @pieces[index - 1].col
        @pieces[index - 1].col ^= @blankCol
        @pieces[index - 1].row ^= @blankRow
        @blankRow ^= @pieces[index - 1].row
        @pieces[index - 1].row ^= @blankRow

    ###
    * judge whether the maze has been completed
    ###
    completed: ->
        index = 1
        while index <= 15
            if (@pieces[index - 1].col - 1) * 4 + @pieces[index - 1].row isnt @pieces[index - 1].id
                return false
            index++
        return true

    ###
    * shuffle the maze randomly
    * @param that: the maze, cuz when in click event, 'this' is DOM event, not maze
    ###
    shuffle: (that)->
        times = 100
        while times > 0
            changeCol = Math.round Math.random()
            movingUp = Math.round Math.random()
            that.randomMove changeCol, movingUp
            times--
        @updatePosition()

    ###
    * auto move randomly
    * @param changeCol: random number(0 or 1), deside change in column position(1) or row position(0)
    * @param movingUp: random number(0 or 1), deside moving up(1) or down(0)
    ###
    randomMove: (changeCol, movingUp)->
        col = @blankCol
        row = @blankRow
        if changeCol
            col = if movingUp and @isValid(col + 1) then col + 1 else if @isValid(col - 1) then col - 1 else col
        else
            row = if movingUp and @isValid(row + 1) then row + 1 else if @isValid(row - 1) then row - 1 else row
        if (col isnt @blankCol or row isnt @blankRow) and (col - 1) * 4 + row isnt 16
            @move (col - 1) * 4 + row

    ###
    * judge whether the position is a valid one
    * @param position: position to judge
    ###
    isValid: (position)->
        return if position >= 1 and position <= 4 then true else false

    ###
    * change background image
    * @param ele: the DOM element for the selected
    ###
    changeBackground: (ele)->
        for piece in @pieces
            piece.element.style.backgroundImage = 'url(' + ele.value + ')'

maze = new Maze

###
* initialize maze when window is loaded
###
window.onload = ->
    maze.initialize()

