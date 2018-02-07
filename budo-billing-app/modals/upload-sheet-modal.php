<!--SUBMIT SHEET MODAL-->
<div class="modal fade" id="upload-sheet-modal" tabindex="-1" role="dialog" aria-labelledby="createLabel"> 
	<div class="modal-dialog" role="document"> 
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
		        <h4 class="modal-title" id="editLabel"><strong>Upload xlsx Sheet</strong></h4>
			</div>
			<div class="modal-body"> 
				<div class="form-group">
					<form action="api/send_email.php" id="reject-user-form" name="sendMail" method="POST" enctype="multipart/form-data">
						<strong><p style="margin-top: 10px; margin-bottom: 8px;">Source</p></strong>
						<input type="file" name="upload_sheet_attached">
						<br>
						</br></br>
						<div class="form-group">
							<button type="submit" class="btn btn-success upload-sheet" name="upload_sheet">Proceed</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>

</div>