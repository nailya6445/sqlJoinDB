@app.route("/")
@login_required
def index():
    """Show reading list"""

    if request.method == "GET":

        # Execute list joining "book" and "idlist" tables
        list = db.execute("SELECT Title, Status, update, Author, Year, Country, Language FROM idlist INNER JOIN book on idlist.Title=book.Title WHERE id=:id",
                          id=session["user_id"])
        # If the user has no list yet
        if not list:
            element = {'Title': "No", 'Author': "No", 'Year': "No", 'Country': "No", 'Language': "No", 'Status': "No", 'Last update': "No"}

    return render_template("index.html")
