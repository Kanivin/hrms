import click

from hrms.setup import before_uninstall as remove_custom_fields


def before_uninstall():
	try:
		print("Removing customizations created by the Kanivin HR app...")
		remove_custom_fields()

	except Exception as e:
		BUG_REPORT_URL = "https://github.com/Kanivin/hrms/issues/new"
		click.secho(
			"Removing Customizations for Kanivin HR failed due to an error."
			" Please try again or"
			f" report the issue on {BUG_REPORT_URL} if not resolved.",
			fg="bright_red",
		)
		raise e

	click.secho("Kanivin HR app customizations have been removed successfully...", fg="green")
