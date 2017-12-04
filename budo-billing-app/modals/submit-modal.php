<!--SUBMIT SHEET MODAL-->
<div class="modal fade" id="submit-modal" tabindex="-1" role="dialog" aria-labelledby="createLabel"> 
	<div class="modal-dialog" role="document"> 
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
		        <h4 class="modal-title" id="editLabel"><strong>Submit for Approval</strong></h4>
			</div>
			<div class="modal-body"> 
				<div class="form-group">
					<form action="api/send_email.php" id="user-submit-for-approval-form" name="sendMail" method="POST" enctype="multipart/form-data">
						<strong><p>Select Recipients</p></strong>
						<!--div class="form-check form-check-inline">
							<input class="form-check-input" type="ratio" id="mark" name="recipients[]" value="mark.cukier@budoholdings.com"> 
							<label> Mark C. </label>
						</div>
						<div class="form-check form-check-inline">
							<input class="form-check-input" type="ratio" id="corey" name="recipients[]" value="corey.fisher@budoholdings.com">
							<label> Corey F. </label>
						</div>
						<div class="form-check form-check-inline">			
							<input class="form-check-input" type="ratio" id="gary" name="recipients[]" value="gary.patzik@budoholdings.com"> 
							<label> Gary P. </label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="mikecaulfield" name="recipients[]" value="mike.caulfield@budoholdings.com" checked="true"> Mike C. 
							</label>
						</div>
						<div class="form-check form-check-inline">
							<label class="form-check-label">
								<input class="form-check-input" type="checkbox" id="boyangdong" name="recipients[]" value="boyang.dong@budoholdings.com"> Boyang D. (notify developer)
							</label>
						</div!-->
						<div class="form-check form-check-inline">
							<input type="radio" id="contactChoice1" name="recipients[]" value="mark.cukier@budoholdings.com">
							<label for="contactChoice1">Mark C.</label>
						</div>
						<div class="form-check form-check-inline">
							<input type="radio" id="contactChoice2" name="recipients[]" value="corey.fisher@budoholdings.com">
						    <label for="contactChoice2">Corey F.</label>
						</div>
						<div class="form-check form-check-inline">
						    <input type="radio" id="contactChoice3" name="recipients[]" value="gary.patzik@budoholdings.com">
						    <label for="contactChoice3">Gary P.</label>
						</div>
						<div class="form-check form-check-inline">
							<input type="radio" id="contactChoice1" name="recipients[]" value="mike.caulfield@budoholdings.com" checked="true">
							<label for="contactChoice1">Mike C.</label>
						</div>
						<div class="form-check form-check-inline">
							<input type="radio" id="contactChoice2" name="recipients[]" value="boyang.dong@budoholdings.com">
						    <label for="contactChoice2">Boyang D. </label>
						</div>
						<br>					
						<strong><p style="margin-top: 5px; margin-bottom: 5px;">Title</p></strong>
						<input type="text" name="mail_sub" class="form-control" value="Today's Rebill Sheet Complete"/>
						<strong><p style="margin-top: 10px; margin-bottom: 5px;">Message</p></strong>
						<textarea rows='6' name="mail_msg" class="form-control" data-error="Please say something..." required>Hi, &#13;&#10;Today's rebill sheet is completed. Please check it out on: &#13;&#10;http://172.30.80.25:8080/budo-billing-app/index.php&#13;&#10;&#13;&#10;Thanks,&#13;&#10;Becky</textarea>
						<!--Attachment Section-->
						<strong><p style="margin-top: 10px; margin-bottom: 8px;">Attachement (optional)</p></strong>
						<input type="file" name="sheet_attached">
						<br><br>
						<!---->
						<div class="form-group">
							<button type="submit" class="btn btn-success send-email" name="send_email">GO!</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>

</div>