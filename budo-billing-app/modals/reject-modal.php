<!--SUBMIT SHEET MODAL-->
<div class="modal fade" id="reject-modal" tabindex="-1" role="dialog" aria-labelledby="createLabel"> 
	<div class="modal-dialog" role="document"> 
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
		        <h4 class="modal-title" id="editLabel"><strong>Reject Back</strong></h4>
			</div>
			<div class="modal-body"> 
				<div class="form-group">
					<form action="api/send_email.php" id="reject-user-form" name="sendMail" method="POST" enctype="multipart/form-data">
						<strong><p>Select Recipients</p></strong>
						<!--div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="becky" name="recipients[]" value="becky.ali@budoholdings.com" checked="true"> Becky A.
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" name="recipients[]" value="mark.cukier@budoholdings.com"> Mark C.
							</label>
						</div>	
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" name="recipients[]" value="corey.fisher@budoholdings.com"> Corey F. 
							</label>
						</div>					
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" name="recipients[]" value="mike.caulfield@budoholdings.com"> Mike C.
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" name="recipients[]" value="phil.pliskin@budoholdings.com"> Phil P.
							</label>
						</div!-->
						<div class="form-check form-check-inline">
							<input type="radio" id="contactChoice1" name="recipients[]" value="becky.ali@budoholdings.com" checked="true">
							<label for="contactChoice1">Becky A. </label>
						</div>
						<div class="form-check form-check-inline">
							<input type="radio" id="contactChoice1" name="recipients[]" value="phil.pliskin@budoholdings.com">
						    <label for="contactChoice2">Phil P.</label>
						</div>
						<br>
						<strong><p style="margin-top: 5px; margin-bottom: 5px;">Title</p></strong>
						<input type="text" name="mail_sub" class="form-control" value="REJECTED: Rebill Sheet Today"/>
						<strong><p style="margin-top: 10px; margin-bottom: 5px;">Message</p></strong>
						<textarea rows='3' name="mail_msg" class="form-control" data-error="Please say something..." required>Hi, please redo the spreadsheet..&#13;&#10;&#13;&#10;Thanks,</textarea>
						</br></br>
						<div class="form-group">
							<button type="submit" class="btn btn-danger send-email" name="send_email">Reject</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>

</div>