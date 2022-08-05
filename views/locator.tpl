% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>


<form method="POST">
    <input name="text">
    <input type="submit">
</form>